import ParseZim


def create(zimpath, fullpath, currentpath):

	html0 = """
	<!DOCTYPE html>
	<html>
	<head>

	<title>Zim</title>

	<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	 
	<link href='"""+fullpath+"""css/style.css' rel="stylesheet" type="text/css" />

	<script>
		var droid = new Android();
		droid.registerCallback('loadnewpage', function(e) {
			document.getElementById('content').innerHTML = e.data;
		});
		function saveChange() {
			changedtext = document.getElementById('txt').value;
			droid.eventPost('save', changedtext);
		}
		function cancelChange() {
			droid.eventPost('cancel', '');
		}
		function clickLink(path) {
			droid.eventPost('link', path)
		}
	</script>

	</head>

	<body>

	<div id="wrapper">"""
	html1 = """</div>

	</body>
	</html>"""

	f = open(zimpath,"r")
	lines = f.readlines()
	f.close()
	
	content = ""

	for line in lines[3:]:
		htmlline = ParseZim.zim2html(line,fullpath,currentpath)
		if htmlline[-3:] == "ul>" or htmlline[-3:] == "li>":
			content += htmlline + "\n"
		else:
			content += htmlline + "<br />\n"

	htmlcontent = """
	<div id="content">"""+content+"""<p></div>
	"""

	return html0 + htmlcontent + html1



def createcontentonly(zimpath, fullpath, currentpath):

	f = open(zimpath,"r")
	lines = f.readlines()
	f.close()
	
	content = ""

	for line in lines[3:]:
		htmlline = ParseZim.zim2html(line, fullpath, currentpath)
		if htmlline[-3:] == "ul>" or htmlline[-3:] == "li>":
			content += htmlline + "\n"
		else:
			content += htmlline + "<br />\n"

	content+="<p>"
	
	return content


def createedit(zimpath, fullpath):

	f = open(zimpath,"r")
	lines = f.readlines()
	f.close()
	
	content = "".join(lines)
	
	form = '''
	<button style='padding:5px; margin:5px;' id='savebtn' type='button' onclick='saveChange();'>
		Save
	</button>
	<button style='padding:5px; margin:5px;' id='cancelbtn' type='button' onclick='cancelChange();'>
		Cancel
	</button><br /><p>
	'''	
	return form+"<textarea id='txt' style='width:99%; min-height:500px;'>"+content+"</textarea>"
