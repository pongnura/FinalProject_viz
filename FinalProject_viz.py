!pip install pandas-bokeh
import streamlit as st
import numpy as np
import pandas as pd
import pandas_bokeh
import seaborn as sns


pandas_bokeh.output_notebook()
pd.set_option('plotting.backend', 'pandas_bokeh')

from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from PIL import Image

st.title('WELCOME! TO "Job Academy"')
st.write("สถาบันจัดหางานที่ดีที่สุดในประเทศไทย")
st.header("Working process 4 Step for Success")

st.subheader("Step 1 : Choose a career")

st.markdown("##The 30 best high-paying job of the future")
need_job = """ Marketing managers Industrial engineers Computer user support specialists Human resources specialists Elementary school teachers  Licensed practical and licensed vocational nurses Speech-language pathologists Industrial machinery mechanics Electricians Sales representatives of services  Substance abuse, behavioral disorder, and mental health counselors Ophthalmologists Construction managers Lawyers Information security analysts Computer systems analysts Computer and information systems managers Management analysts Market research analysts and marketing specialists Software developers and software quality assurance analysts and testers""" 

plt.subplots(figsize=(8,8))
wordcloud = WordCloud(
                    background_color='white',
                    width=512,
                    height=384
                    ).generate(need_job) #เอาทุกคำใน list มา join กันด้วย space bar (เปลี่ยนใน join จาก x2011 เป็น)
                    
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png') #save image
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


st.markdown("##S o f t w a r e d e v e l o p e r s k i l l s")
text_try = """Hello friends, If you have been doing software development for some time and thinking about what makes a good programmer? What should a programmer learn in 2020 to become a better developer? What should computer science graduates can learn in advance for a career in software development and programming?
			What are the skills expected of a junior developer are some of the common questions I receive from many students on Facebook and Emails who follows me.
			These are mostly college graduates and beginners who now have access to a wealth of information thanks to the internet and eager to learn skills in advance to prepare for their programming job interviews.
			In this article, I’ll share 11 skills, which I believe, every programmer should know or learn in 2020.
			This includes a programming language like C++ or Java, essential computer science concepts like Data Structures, Algorithms and Computer Network basics, crucial tools like Git, Docker, Kubernetes and containers in general, Cloud computing concepts and platforms like AWS, GCP, Microsoft Azure, and evergreen skills like SQL and UNIX, editors like Eclipse or Visual Studio Code, and text editors, like VIM and NotePad++, etc.
			This list is by no means complete, but it provides you a good starting point for skills a programmer should know. If you are aiming for a career in software development and looking for a programming job, then these are things you can learn and improve to stay ahead of your competition.
			Top 11 Essentials Skills for Software Developers in 2020
			Without further ado, here is a list of skills which I personally believe, every programmer should know, irrespective of the job he is doing. These are essential skills and will serve you for a long time. Any investment made into this in terms of time, money, and effort will help you to reap the rewards throughout your career.
			1. Cloud Computing Skills (AWS, GCP, or Azure)
			Apart from containers, Cloud is another thing which I think every Software developer and Data Scientist should learn in 2020. Companies of all sizes and domains are now shifting their environments into Cloud for cost-saving and better scalability, which means sooner or later, you need to work with cloud-native applications.
			They are also essential for all the sunrise development in the field of Data Science, Machine Learning, and Artificial intelligence because the only cloud can provide the computing power needed by those resource-hungry models.
			Learning Cloud platforms like Amazon Web Service (AWS), Google Cloud Platform (GCP) or Microsoft Azure will take you one step ahead of your competitors not only in your current job but also in the next post. You don’t need to learn all of them, and in fact, learning one means you will have a fair idea about others.
			To start with, I suggest you learn AWS as it is the most popular and most mature cloud platform and there is a strong demand of developers and system admins with AWS knowledge if you need a resource then I recommend the Ultimate AWS Certified Solutions Architect Associate course by Stéphane Maarek, the Cloud Guru. It will not only help you learn AWS in-depth but also prepare you for AWS certification.
			Image for post
			2. Data Structure and Algorithms
			If you want to become a programmer, then you ought to know Data Structure and Algorithms well; there is no escape. This is one of the important topics of any programming job interview, and without you knowing basic data structures, like an array, linked list, map, set, it’s not possible to write a real-world application.
			That’s why every programmer should put a serious effort into learning the Data structure and Algorithm during their computer science course.
			If you are a self-taught programmer, then also you must know Data structure and algorithm; in fact, many programming bootcamp will teach you Data structure and algorithm as the first thing. If you need a course then I highly recommend checking out Data Structures and Algorithms: Deep Dive Using Java course by Tim Buchalaka on Udemy.
			Image for post
			And, if you need free resources to learn Data Structure and Algorithms then you can check these free Algorithms courses on Medium.
			3. Git and Github
			Source control is used to store code, and if you want to become a coder or software developer, you must know version control tools like Git and SVN.
			Thankfully Git and Github have streamlined the market, and now more than 70% organization uses Git; hence you can get away by just learning Git.
			Btw, you should put some effort into learning Git well, like you should be comfortable with advanced version control concepts like branching and merging as well as the tool itself, I mean, both on the command line and using GUI. For beginners, The GitHub Ultimate: Master Git and GitHub is the right place to start with.
			Image for post
			And, If you need a free online course to learn Git, check out these free Git courses on Medium
			4. Containers (Docker and Kubernetes)
			In 2020, I believe every programmer, software engineer, data scientist, and even project manager should know about containers and tools like Docker and Kubernetes.
			It’s proven now that containers like Docker not only help developers to test their application in a unified environment but also they simplify the deployment process.
			With the help of Docker, you can quickly deploy your application with all of its dependency in one shot, it also provides you process isolation. Similarly, Kubernetes, which is a container orchestration tool, takes it to the next level and can manage containers for you.
			This means you no need to worry about the Scalability of your application, and Kubernetes or K8s can do that for you automatically. If you want to learn a new skill in 2020, I suggest you learn Docker and Kubernetes, it will not only help in your current job but also in the next post as they are also the most sought after skill by companies on all sizes.
			And, if you have already realized the importance of containers and looking for a resource to learn Docker and Kubernetes, I suggest you join Stephen Grider’s best selling course — Docker and Kubernetes: The Complete Guide, one of the best course to learn these two essential skills.
			Image for post
			And, if you need some free course materials then I also suggest you check out these free Docker courses to start with.
			5. VIM
			There is not a single day when I have not used a text editor while working as programmers. It’s one of the essential tools even for non-programmers and anyone who works with computers.
			I have mostly used NotePad on Windows and VIM in Linux, but nowadays, you have a lot of choices available in terms of advanced editors like Sublime and NotePad++, which provides IDE like functionalities.
			I suggest you to spend some time learning your favorite Editor and keyboard shortcuts, productivity tips are something you can learn. If you like VIM, then go ahead and learn VIM, you will not regret your decision. If you need a recommendation then VIM MasterClass by Jason Cannon is an excellent course to learn such skills.
			Image for post
			And, if you need more choices, check out my article on best VIM courses which has a few more options to learn VIM in depth.
			6. IDEs (VSCode or IntelliJIDEA)
			The modern IDES like Eclipse or Visual Studio Code is the most critical tool for any programmers. For C, C++, and C# programmer, the choice is clear, the Visual Studio and for Python developers, Jupiter Notebook is getting better and better every day.
			If you want to learn VS Code, I suggest you join Learn Visual Studio Code by James Quick on Udemy.
			Image for post
			For Java Programmers, there are three primary IDE to choose, like Eclipse, NetBeans, and IntelliJ, while Eclipse is my favorite, IntelliJIDEA is not bad at all.
			If you want to learn IDEA better than you can also check out IntelliJIDEA Tricks to boost Productivity course by TAO W and James Lee
			Image for post
			7. Database and SQL
			SQL is a classic, it’s been around for more than 30 years, and I think it will be around for another 30 years. Given the omnipresence of the database, it’s expected from a programmer that he is familiar with essential database concepts like normalization and table design along with SQL.
			There are many databases, like Oracle, MySQL, Microsoft SQL Server, PostgreSQL, etc. but knowing just one is enough. The critical point is that you should be familiar with the database. You should know how to insert/update/delete data and write SQL queries to retrieve it.
			Knowledge of advanced concepts like join an aggregate function is a big bonus, and if you want to get that, then The Complete SQL BootCamp by Jose Marcial Portilla is a great course to start with.
			Image for post
			And, if you need free resources then these free SQL courses on Medium are a great place to start with.
			8. Linux (UNIX)
			Like SQL, UNIX also has withstood the test of time. It’s also been around for more than 30 years, and I hope it will there for many more coming years. Since most of the time, programmers have to work in the UNIX machine, like Linux servers, good knowledge of the Linx command line goes a long way.
			It allows you to work effectively. You can search files, know what’s going on with the system by checking its CPU and memory usage, and perform basic and advanced tasks.
			If you want to learn Linux commands, I suggest to go through Learn Linux in 5 Days and Level Up Your Career course on Udemy
			Image for post
			And, if you need some free resources to start with then you can also check out these free Linux courses on Medium.
			9. Object-Oriented Programming
			As a programmer, you must know a programming language like C++ or Java or maybe Python or JavaScript. You can choose whatever you want to, but my personal suggestion is that you should at least know Java.
			It’s straightforward to start with, and that’s why the right choice for beginners. It’s also immensely powerful and allows you to virtually anything.
			It has got libraries from doing basic stuff, like web development to Big Data and so on. If you decide to learn Java, then The Complete Java MasterClass is probably the best place to start with.
			Image for post
			And, if you need some free alternatives to learn Java, then these free Java courses are probably the best place to start with.
			10. Computer Networks
			Today’s world is an interconnected world, and anywhere you go, you will find computer networks, starting from home where you are using WIFI across many devices to school, college, and offices, which uses Local Area Network (LAN) to the Internet.
			Most of the applications you will write will also not be standalone, but the client-server kind of use where the request will go through the network to a server. Clients will access your application from anywhere in the world.
			The bottom line is that you must understand the networking basics to understand, develop, and support your application.
			If you want to learn more, then I suggest you join The Complete Networking Fundamentals course on Udemy. A good starting point for beginners.
			Image for post
			11. Scripting
			In point # 8, I have asked you to learn a Programming language, and here I am asking you to learn a scripting language? Why? Can the same programming language not be used as a scripting language?
			Well, there is undoubtedly some language which is suitable for both OOP coding and scripting like Python, and that’s why I asked you to learn it at least, but if you happen to learn C/C++ or Java, then you can’t whip out something as quickly as a Python or Perl developer can do.
			If you want to learn Python and need a course, The Complete Python Bootcamp is a great course to start with.
			Image for post
			The scripting language makes it easy to create tools and scripts to solve common problems in the programming world. If you have a good command over a scripting language, like Python, then you can automate mundane stuff easily.
			Once again, I suggest you to learn Python to kill two birds in one stone, and if you need some more resources, this list of free Python tutorials from Microsoft and Google is also beneficial.
			That’s all about 11 skills every Programmer should learn. Computer science graduates and people who aspire to become programmers can use this list to find out about things like tools and skills to become a successful programmer.
			Btw, if you are interested to learn more about things programmers should know, there is a lot of guidance available in terms of essential stuff for programmers, and you can find man great advice on the internet like 97 Things Programmer should know, a must-read for every serious programmer.
			Other Programming articles you may like
			10 Algorithm Books Every Programmer Should Read
			10 Tools Every Software Engineer should know
			The 2020 Java Developer RoadMap
			10 High Paying Career Options for Programmers and developers
			10 Tips to become a better Java developer
			The Complete Web Developer RoadMap
			10 Tips to Improve your Programming Skill
			10 OOP Design Principles Every Programmer Should Know
			100+ Data Structure and Algorithm Questions for Programmers
			10 Unit testing tools for Java Programmers
			Thanks for reading this article so far. If you find this article useful, then please share it with your friends and colleagues. If you have any questions or feedback, then please drop a note.
			If you think I have missed a critical skill which is beneficial for a programmer and one should learn it, feel free to suggest and I would be happy to incorporate it into this article. After all, Programming is a journey, and every day we learn something important."""

wordcloud = WordCloud(
			background_color='white',
			width=512*2,
			height=384*2).generate(text_try)
			                    
plt.axis('off')
plt.imshow(wordcloud)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# (Atomm Pie)
st.markdown('##Software developer skills')
img = Image.open("/Users/natty/Beam/pie.jpg")
st.image(img, width=700, caption="Software developer skills")



st.subheader("Step 2 : Insight client")

#1
st.write("Beam's skills in 4 years")

col1 = list(['Year 1.1', 'Year 1.2','Year 2.1','Year 2.2', 'Year 3.1', 'Year 3.2', 'Year 4.1', 'Year 4.2'])
col2 = list([3, 5, 6, 7, 8, 8.5, 9, 9])
col3 = list([2, 3, 6, 8, 5, 5, 8, 8])
col4 = list([5, 5, 6, 4, 4, 6, 7, 8,])

my_skill = pd.DataFrame({
    'Years' : np.array(col1),
    'StatisticalSkills' : np.array(col2),
    'ComputerSkill' : np.array(col3),
    'SoftSkill' : np.array(col4)
})

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(16,5))
axes.plot(col1, col2, marker = 'o', color = 'gray')
axes.plot(col1, col3, marker = 'o', color = 'tomato')
axes.plot(col1, col4, marker = 'o', color = 'gray')
plt.grid(b=None)
plt.title("Beam's score vs Candidates")
axes.legend(['SoftSkill','ComputerSkill','StatisticalSkills'],fontsize=12, loc='lower left')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#2
st.write("Beam's score vs Candidates")

skill = ['Language Skill','Programming Skill','Problem Solving Skill','Mathematical Skill']

Beam = [85,80,78,85]
Beam_label = ['85','80','78','85']

Candidate_A = [30,66,64,47]
Candidate_B = [80,50,50,60]
Candidate_C = [64,31,26,33]
Candidate_D = [67,43,56,74]
Candidate_E = [48,67,51,68]

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(16,5))
axes.plot(skill, Beam, marker = 'o', color = 'tomato')
axes.plot(skill, Candidate_A, marker = 'o', color = 'gray')
axes.plot(skill, Candidate_B, marker = 'o', color = 'gray')
axes.plot(skill, Candidate_C, marker = 'o', color = 'gray')
axes.plot(skill, Candidate_D, marker = 'o', color = 'gray')
axes.plot(skill, Candidate_E, marker = 'o', color = 'gray')
plt.grid(b=None)
plt.title("Beam's score vs Candidates")
axes.legend(['Beam'],fontsize=12, loc='lower left')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


st.subheader("Step 3 : Compare features")

#1
st.write("Compare salary between 'iA Group' and 'ecosoft'")

salary = [20000,25000]
distance = [11.2,16.4]
compare_company = pd.DataFrame({'Salary (Baht)': np.array(salary) , 
				'Distance (km) ': np.array(distance), 'Company': ['ecosoft','iA Group']})
compare_company.set_index('Company')
salary = []
for elem in range(0,25000):
        salary.append("iA Group")
for elem in range(0,20000):
        salary.append("ecosoft")
compare_salary = pd.DataFrame({"salary": np.array(salary)})
plt.figure(figsize=(6,2))
salary_Comp = sns.countplot(y=compare_salary['salary'],palette="Set2")
plt.title("Compare salary between 'iA Group' and 'ecosoft'")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#2 distance

st.write("Distance between Beam's Apartment and Companies")

lat_loc = [13.706556,13.719236,13.757103]
long_loc = [100.599329,100.521511,100.533864]
compare_location = pd.DataFrame({"Latitude": lat_loc, "Longitude": long_loc , 'Location': ["Beam's Apartment",'ecosoft','iA Group']})
compare_location.set_index('Location')

st.write(compare_location.plot_bokeh.map(
    x="Longitude",
    y="Latitude",
    tile_provider="CARTODBPOSITRON_RETINA",
    size = 20,
    figsize=(600, 500),color='tomato'))

#3 
st.header('Transportation')
img = Image.open("/Users/natty/Beam/map.jpg")
st.image(img, width=700, caption="Transportation")


#4
time = ['0','1','2','3']
IA_Group = [0,20,10,5]
Ecosoft = [0,10,25,20]
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(16,5))
axes.plot(time,IA_Group, label='IA Group',marker = 'o')
axes.plot(time,Ecosoft,label='Ecosoft',marker = 'o',color = 'red')
axes.set_title('time for public car ', fontsize=25)
axes.set_xlabel('period', fontsize=15)
axes.set_ylabel('time(minute)', fontsize=15)
axes.legend()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

time1 = ['0','1','2']
IAGroup = [0,20,10]
ecosoft = [0,15,35]
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(16,5))
axes.plot(time1,IAGroup, label='IA Group',marker = 'o' )
axes.plot(time1,ecosoft,label='Ecosoft',marker = 'o',color = 'red')
axes.set_title('time for personal car ', fontsize=25)
axes.set_xlabel('period', fontsize=15)
axes.set_ylabel('time(minute)', fontsize=15)
axes.legend()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.subheader("Step 4 : Choose Company")





