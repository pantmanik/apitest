from flask import Flask, request, jsonify
import urllib
from color_pick import ColorFinder

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb

def clean_url(url):
	path=urllib.parse.urlparse(url).path
	path=urllib.parse.quote(path)
	netloc=urllib.parse.urlparse(url).netloc
	scheme=urllib.parse.urlparse(url).scheme
	finurl=urllib.parse.urlunparse((scheme,netloc,path,'','',''))
	return finurl

app = Flask(__name__)


@app.route('/')
def index():
	url=request.args.get('src')

	finurl=clean_url(url)

	# img=urllib.parse.urlunsplit((addressing_scheme, network_location, path, query, fragment_identifier))
	cf=ColorFinder(finurl)
	dom_colors=cf.dominantColors()
	bor_color=cf.borderColor()
	# dominant=rgb_to_hex(tuple(colors[0]))
	dominant="#"+str(rgb_to_hex(tuple(dom_colors[0]))).upper()
	border="#"+str(rgb_to_hex(tuple(bor_color))).upper()
	output=jsonify({'dominant_color':dominant,
					'border_color':border})
	return output
	# return "#"+str(rgb_to_hex((255,255,255)))





if __name__ == '__main__': app.run(debug=True)