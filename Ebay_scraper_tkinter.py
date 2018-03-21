from bs4 import BeautifulSoup as soup
import urllib.request
import urllib.parse
import webbrowser

class basic_window:
    def __init__(self,master):
        
        self.v = StringVar()
        Entry(master,textvariable=self.v).grid(row=0)
        Button(master,text='Search in ebay',command=self.search).grid(row=1)
        self.r=2
    
    def search(self):
        
        self.string = self.v.get()
        url = 'https://www.ebay.com/sch'
        self.values = {"_nkw":self.string}
        self.data = urllib.parse.urlencode(self.values)
        self.data = self.data.encode('utf-8')
        
        headers= {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'
        
        self.req = urllib.request.Request(url,self.data,headers=headers)
        self.source = urllib.request.urlopen(self.req)
        self.page_html = self.source.read()
        self.page_soup = soup(self.page_html,"html.parser")
        
        self.containers = self.page_soup.find_all("li",{"class":"sresult lvresult clearfix li shic"})
        
        for self.container in self.containers:
            
            self.title = self.container.find("img").attrs['alt']
            Label(root,text=self.title).grid(row=self.r)
            
            self.link = self.container.find("a").attrs['href']
            Button(root,text='Go to link',command=self.link_open).grid(row=self.r,column=1)

            self.r+=1
    
    def link_open(self):
        webbrowser.open(self.link)
        

root = Tk()
obj = basic_window(root)
root.mainloop()
