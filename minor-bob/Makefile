.PHONY: tiles

tiles:
	blender -b tileset.blend -P generate_tiles.py
	montage tiles/tile*.png -tile 6x3 -geometry 64x128+0+0 -background transparent tileset.png
