#!/usr/bin/env python

import lx
import modo


def main():
		modo.util.makeQuickCommand('mm.render', render, [('anim', False), ('ptagType', True)])
		modo.util.makeQuickCommand('mm.rand', randomize)
		modo.util.makeQuickCommand('mm.setval', setVal, [('value', '0')])


def render(anim, ptagType):
	scene = modo.Scene()
	addedItems = []
	tags = []

	#Create lists of unique material tags
	if ptagType:
		for item in scene.items():
			if item.type == 'mask':
				ptag = item.channel('ptag').get()
				if ptag not in tags:
					tags.append(ptag)

	#Create list of unique mmVals
	else:
		for mesh in scene.meshes:
			try:
				tag = mesh.channel('mmVal').get()
				if tag not in tags:
					tags.append(tag)
			except:
				pass

		#Create groups per tag
		for tag in tags:
			group = scene.addGroup('mmTag%s' % tag)
			for mesh in scene.meshes:
				try:
					if mesh.channel('mmVal').get() == tag:
						group.addItems(mesh)
						addItems.append(group)
				except:
					pass

	#Create new render pass group
	passGroup = scene.addRenderPassGroup('mmPasses')

	#Find the number of passes to be created
	if len(tags) % 3 == 0:
		passCount = len(tags) / 3
	else:
		passCount = (len(tags) / 3) + 1

	#Add passes to our render pass group
	renderPasses = []
	for renderPass in range(passCount):
		renderPasses.append(passGroup.addPass('mmPass%s' % renderPass))
		addedItems.append(renderPasses[-1])

	#Create material group containing a plain shader at the top of the shader tree
	containerMask = scene.addItem('mask', 'mmContainer')
	containerMask.select()
	lx.eval('texture.parent polyRender006 -1')
	containerMask.deselect()
	containerShader = scene.addItem('defaultShader', 'mmShader')
	containerShader.setParent(scene.item('mmContainer'))
	addedItems.append(containerMask)
	addedItems.append(containerShader)

	#Add masks and materials per material tag, add to material group
	masks = []
	for i, tag in enumerate(tags):
		mask = scene.addItem('mask', 'mmMask%s' % tag)
		mat = scene.addMaterial('advancedMaterial', 'mmMat%s' % tag)
		mat.setParent(mask)
		mask.setParent(scene.item('mmContainer'))
		if ptagType:
			mask.channel('ptag').set(tag)
		else:
			mask.select()
			lx.eval('mask.setMesh mmTag%s' % tag)
			mask.deselect()

		#Every third material will be red, green, or blue
		if (i + 1) % 3 == 2:
			rgb = [1, 0, 0]
		elif (i + 1) % 3 == 1:
			rgb = [0, 1, 0]
		else:
			rgb = [0, 0, 1]

		#Set material channels
		matChannels = {'diffAmt': 0,
						'specAmt': 0,
						'specFres': 0,
						'radiance': 1,
						'lumiCol.R': rgb[0],
						'lumiCol.G': rgb[1],
						'lumiCol.B': rgb[2]}
		for channel in matChannels.keys():
			mat.channel(channel).set(matChannels[channel])

		masks.append(mask)
		addedItems.append(mask)
		addedItems.append(mat)

	#Add a black material to the bottom of the material group
	mat = scene.addMaterial('advancedMaterial', 'mmBlack')
	mat.setParent(scene.item('mmContainer'))
	matChannels = {'diffAmt': 0,
					'specAmt': 0,
					'specFres': 0,
					'radiance': 0}
	for channel in matChannels.keys():
		mat.channel(channel).set(matChannels[channel])
	addedItems.append(mat)

	#Turn masks on and off in render passes
	for i, renderPass in enumerate(renderPasses):
		masksOn = range(i * 3, (i + 1) * 3)
		for n, mask in enumerate(masks):
			if n not in masksOn:
				renderPass.setValue(mask.channel('enable'), False)

	#Set up black background
	env = scene.addItem('envMaterial', 'mmTmpEnv')
	env.select()
	lx.eval('texture.parent shaderFolder008 -1')
	env.deselect()
	env.channel('type').set('constant')
	env.channel('zenColor').set((0, 0, 0))
	addedItems.append(env)

	render = modo.Item('polyRender006')
	userGi = render.channel('globEnable').get()
	render.channel('globEnable').set(False)
	addedItems.append(passGroup)  #Added this last to fix crashes when deleting items

	if anim:
		params =	(render.channel('first').get(),
					render.channel('last').get(),
					render.channel('step').get(),
					addedItems[-1].id)
		try:  #User may cancel this opperation
			lx.eval('render.animationDialog %s %s %s sequence %s' % params)
		except:
			pass
	else:
		lx.eval('render.passes %s' % addedItems[-1].id)

	scene.removeItems(addedItems)
	render.channel('globEnable').set(userGi)


def randomize():
	scene = modo.Scene()
	channelNames = []
	userSelection = scene.selected
	for item in scene.items():
		item.deselect()
	for i, item in enumerate(scene.meshes):
		for channel in item.channels():
			channelNames.append(channel.name)
		if 'mmVal' not in channelNames:
			item.select()
			lx.eval('channel.create mmVal integer username:mmVal')
			item.deselect()
			item.channel('mmVal').set(i)
		channelNames = []
	for item in userSelection:
		item.select()

def setVal(value):
	scene = modo.Scene()
	channelNames = []
	userSelection = scene.selected
	for item in scene.items():
		item.deselect()
	for item in userSelection:
		for channel in item.channels():
			channelNames.append(channel.name)
		if 'mmVal' in channelNames:
			item.channel('mmVal').set(value)
		else:
			item.select()
			lx.eval('channel.create mmVal integer username:mmVal')
			item.deselect()
			item.channel('mmVal').set(value)
		channelNames = []
	for item in userSelection:
		item.select()



main()
