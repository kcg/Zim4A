def zim2html(l0, fullpath, currentpath):
	
	#BLOCK
	
	# Headings
	if "======" in l0:
		return "<h1>"+l0.replace("======","").lstrip()[:-1]+"</h1>\n"
	if "=====" in l0:
		return "<h2>"+l0.replace("=====","").lstrip()[:-1]+"</h2>\n"
	if "====" in l0:
		return "<h3>"+l0.replace("====","").lstrip()[:-1]+"</h3>\n"
	if "===" in l0:
		return "<h4>"+l0.replace("===","").lstrip()[:-1]+"</h4>\n"
	if "==" in l0:
		return "<h5>"+l0.replace("==","").lstrip()[:-1]+"</h5>\n"
		
	# Lists
	if l0[0:2] == "* ":
		return "<ul><li>"+l0[2:-1]+"</li></ul>"
		
	# Checkbox
	if "[ ]" in l0:
		return "<ul><li class='unchecked-box'>"+l0[4:]+"</li></ul>"
	if "[*]" in l0:
		return "<ul><li class='checked-box'>"+l0[4:]+"</li></ul>"
	if "[x]" in l0:
		return "<ul><li class='xchecked-box'>"+l0[4:]+"</li></ul>"
		
	# Lines
	if "-----------------------------------------------" in l0 or "___________________________________________" in l0:
		return "<hr/>"
	
	
	#INLINE
	
	wholeline = ""
	for l in l0.split(" "):	
		# Markup
		out = l
		if "**" in l:
			out =  "<b>"+l.replace("**","")+"</b>"
		if "//" in l:
			out =  "<i>"+l.replace("//","")+"</i>"
		if "__" in l and not "___" in l:
			out =  "<u>"+l.replace("__","")+"</u>"
		if "''" in l:
			out =  "<pre>"+l.replace("''","")+"</pre>"
		if "~~" in l:
			out =  "<s>"+l.replace("~~","")+"</s>"
		
		# Images
		if "{{" in l:
			out =  "<img style='width:90%;' src='"+currentpath[:-4]+"/"+l.replace("{{","").replace("}}","").replace("./","")+"' />"

		# Links
		if "[[" in l:
			ls = l.replace("[[","").replace("]]","")
			if ":" in l:
				out =  "<a href='#' onClick='clickLink(\""+ls+".txt\");'>"+ls+"</a>"
			elif "+" in l:
				out =  "<a href='#' onClick='clickLink(\""+ls+".txt\");'>"+ls+"</a>"
			elif "|" in l:
				i = l.find("|")
				a = y[:i]
				b = y[i+1:]
				out =  "<a href='#' onClick='clickLink(\""+a+".txt\");'>"+b+"</a>"
			else:
				out =  "<a href='#' onClick='clickLink(\""+ls+".txt\");'>"+ls+"</a>"
		wholeline += out + " "
	return wholeline
