e=[]
print("""<html>
""")
e.append("""<html>
""")
print("""    <head>
""")
e.append("""    <head>
""")
print("""        <title>
""")
e.append("""        <title>
""")
print("""            
""")
e.append("""            
""")
print("""            MyPage
""")
e.append("""            MyPage
""")
print("""        </title>""")
e.append("""        </title>""")
print("""        <script>
""")
e.append("""        <script>
""")
print("""            alert("hello friends")
""")
e.append("""            alert("hello friends")
""")
print("""        </script>""")
e.append("""        </script>""")
print("""        
""")
e.append("""        
""")
print("""    </head>""")
e.append("""    </head>""")
print("""    <body>
""")
e.append("""    <body>
""")
print("""        <div>
""")
e.append("""        <div>
""")
print("""            The list
""")
e.append("""            The list
""")
print("""            e=fun(e)
""")
e.append("""            e=fun(e)
""")
i in range(12):

print(f"<div id='divname{i+1}'> {i+1}</div>")

e.append(f"<div id='divname{i+1}'> {i+1}</div>")

print("""        </div>""")
e.append("""        </div>""")
print("""        
""")
e.append("""        
""")
print("""    </body>""")
e.append("""    </body>""")
print("""</html>""")
e.append("""</html>""")

htmlfile=open("htmlfinal.html","w")
for line in e:
    htmlfile.write(line)
htmlfile.close()