#!/usr/bin/env python

import lx
import modo


def main():
	modo.util.makeQuickCommand('mm.render', render, [('anim', False), ('ptag_type', True)])
	modo.util.makeQuickCommand('mm.rand', randomize)
	modo.util.makeQuickCommand('mm.setVal', set_val, [('value', '0')])


def render(anim, ptag_type):
	scene = modo.Scene()
	added_items = []
	tags = []

	#Create lists of unique material tags
	if ptag_type:
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
			group = scene.addGroup('mmTag{}'.format(tag))
			for mesh in scene.meshes:
				try:
					if mesh.channel('mmVal').get() == tag:
						group.addItems(mesh)
						addItems.append(group)
				except:
					pass

	#Create new render pass group
	pass_group = scene.addRenderPassGroup('mmPasses')

	#Find the number of passes to be created
    tags_count = len(tags)
    pass_count = tags_count / 3 if tags_count % 3 == 0 else tags_count / 3 + 1

	#Add passes to our render pass group
	render_passes = []
	for render_pass in range(pass_count):
		render_passes.append(pass_group.addPass('mmPass{}'.format(render_pass)))
		added_items.append(render_passes[-1])

	#Create material group containing a plain shader at the top of the shader tree
	container_mask = scene.addItem('mask', 'mmContainer')
	container_mask.select()
	lx.eval('texture.parent polyRender006 -1')
	container_mask.deselect()
	container_shader = scene.addItem('defaultShader', 'mmShader')
	container_shader.setParent(scene.item('mmContainer'))
	added_items.append(container_mask)
	added_items.append(container_shader)

	#Add masks and materials per material tag, add to material group
	masks = []
	for i, tag in enumerate(tags):
		mask = scene.addItem('mask', 'mmMask{}'.format(tag))
		mat = scene.addMaterial('advancedMaterial', 'mmMat{}'.format(tag))
		mat.setParent(mask)
		mask.setParent(scene.item('mmContainer'))
		if ptag_type:
			mask.channel('ptag').set(tag)
		else:
			mask.select()
			lx.eval('mask.setMesh mmTag{}'.format(tag))
			mask.deselect()

		#Every third material will be red, green, or blue
        channel_selection = (i + 1) % 3
		if channel_selection == 2:
			rgb = [1, 0, 0]
		elif channel_selection == 1:
			rgb = [0, 1, 0]
		else:
			rgb = [0, 0, 1]

		#Set material channels
		material_channels = {
            'diffAmt': 0,
			'specAmt': 0,
			'specFres': 0,
			'radiance': 1,
			'lumiCol.R': rgb[0],
			'lumiCol.G': rgb[1],
			'lumiCol.B': rgb[2]
        }
		for channel in material_channels.keys():
			mat.channel(channel).set(material_channels[channel])

		masks.append(mask)
		added_items.append(mask)
		added_items.append(mat)

	#Add a black material to the bottom of the material group
	mat = scene.addMaterial('advancedMaterial', 'mmBlack')
	mat.setParent(scene.item('mmContainer'))
	material_channels = {
        'diffAmt': 0,
		'specAmt': 0,
		'specFres': 0,
		'radiance': 0
    }
	for channel in material_channels.keys():
		mat.channel(channel).set(material_channels[channel])
	added_items.append(mat)

	#Turn masks on and off in render passes
	for i, render_pass in enumerate(render_passes):
		masks_on = range(i * 3, (i + 1) * 3)
		for n, mask in enumerate(masks):
			if n not in masks_on:
				render_pass.setValue(mask.channel('enable'), False)

	#Set up black background
	env = scene.addItem('envMaterial', 'mmTmpEnv')
	env.select()
	lx.eval('texture.parent shaderFolder008 -1')
	env.deselect()
	env.channel('type').set('constant')
	env.channel('zenColor').set((0, 0, 0))
	added_items.append(env)

	render = modo.Item('polyRender006')
	user_gi = render.channel('globEnable').get()
	render.channel('globEnable').set(False)
	added_items.append(pass_group)  #Added this last to fix crashes when deleting items

	if anim:
		parameters = (
            render.channel('first').get(),
			render.channel('last').get(),
			render.channel('step').get(),
			added_items[-1].id
        )
        #User may cancel this opperation
		try:  
			lx.eval('render.animationDialog {} {} {} sequence {}'.format(*parameters))
		except:
			pass
	else:
		lx.eval('render.passes {}'.format(added_items[-1].id))

	scene.removeItems(added_items)
	render.channel('globEnable').set(user_gi)


def randomize():
	scene = modo.Scene()
	channel_names = []
	user_selection = scene.selected
	for item in scene.items():
		item.deselect()
	for i, item in enumerate(scene.meshes):
		for channel in item.channels():
			channel_names.append(channel.name)
		if 'mmVal' not in channel_names:
			item.select()
			lx.eval('channel.create mmVal integer username:mmVal')
			item.deselect()
			item.channel('mmVal').set(i)
		channel_names = []
	for item in user_selection:
		item.select()

def set_val(value):
	scene = modo.Scene()
	channel_names = []
	user_selection = scene.selected
	for item in scene.items():
		item.deselect()
	for item in user_selection:
		for channel in item.channels():
			channel_names.append(channel.name)
		if 'mmVal' in channel_names:
			item.channel('mmVal').set(value)
		else:
			item.select()
			lx.eval('channel.create mmVal integer username:mmVal')
			item.deselect()
			item.channel('mmVal').set(value)
		channel_names = []
	for item in user_selection:
		item.select()


main()
