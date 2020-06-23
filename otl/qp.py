import re
import string
import random

class Option:
	def __init__(self, choice, ans):
		self.choice = choice
		self.ans = ans

class Mcq:
	def __init__(self, text):
		reg = re.compile(r'(.*)\no\)(.*)\no\)(.*)\no\)(.*)\no\)(.*)\n(\d)')
		fragments = reg.search(text)
		self.question = fragments.group(1)
		self.options = []
		count =2
		while(count <= 5):
			myoption = Option(fragments.group(count), int(fragments.group(6)) == count-1)
			self.options.append(myoption)
			count+=1
			
		

class qp:
	def __init__(self, filename):
		f = open(filename)
		text = f.read()
		reg = re.compile(r'.*\no\).*\no\).*\no\).*\no\).*\n\d')
		fragments = reg.findall(text)
		self.fullset = []
		for elt in fragments:
			mymcq = Mcq(elt)
			self.fullset.append(mymcq)
	def olotpalot(self):
		random.shuffle(self.fullset)
		for elt in x.fullset:
			random.shuffle(elt.options)
				

if __name__ == "__main__":
	x=qp('qp.dat')
	y=['1','2','3','4','5','6','7','8','9','10']
	#x.olotpalot()
	file=open("question.html", "w")
	file.write('{% extends "base.html" %}\n\n')
	file.write('{% block content %}\n')
	file.write('<form method="POST">\n')
	file.write('{% csrf_token %}\n')
	file.write('\t{{ form.non_field_errors }}\n')
	file.write('\t{{ form.source.errors }}\n')
	file.write('\t{{ form.source }}\n')
	file.write('<div class="well">\n')
	file.write('<ol>\n')
	for elt, ans in zip(x.fullset, y):
		file.write('<p>\t<li>')
		file.write(elt.question)
		file.write('\n')
		file.write('\t\t<ol>\n')
		for opt in elt.options:
			file.write('\t\t\t<li>')
			file.write(opt.choice)
			file.write('\n')
		file.write('\t\t</ol>\n')
		file.write('\t{{ form.AnsQ' + ans + '.label_tag }}\n')
		file.write('\t{{ form.AnsQ' + ans + '.errors }}\n')
		file.write('\t{{ form.AnsQ' + ans + ' }}\n')
		file.write('</p>\n')
	file.write('</ol>\n')
	file.write('</div>\n')
	file.write('<input type="submit" value="submit" class="btn btn-primary btn-lg">\n')
	file.write("</form>\n")
	file.write("{% endblock %}\n")
	file.close()
	
