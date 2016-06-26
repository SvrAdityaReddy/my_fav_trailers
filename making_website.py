import webbrowser
import os

html='''

<html>
    <head>
        <title>Movies Trailer Website</title>
        <style type=text/css media="screen">
        @font-face {
        font-family: Contail One;
        src: url('contrail_one.ttf') format('truetype');
            }
        div.images {
            padding: 30px 30px;
            float: left;
            }
        header {
            background-color: #242323;
            color: #EFEFEF;
            padding: 20px 50px;
            font-family: 'Contail One';
            font-size: 3em;
            }
        div.images figure#trail > img {
            display: block;
            position: relative;
            overflow: hidden;
            width: 100%;
            height: auto;
            }
        div.images figure#trail > figcaption {
            display: block;
            text-align: left;
            font-weight: 800;  
            font-size: 1em;
            display: table-caption; caption-side: bottom ;
            }
        figure {
            display: table;
            width: 250px;
            height: 180px
            }
        </style>
        
    
    </script>
    <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.0.0.min.js"></script>
    <script>
        $(function(){
           //alert('hello'); 
           $('body section#movies div.images > figure#trail').delegate('img,figcaption','click',function(){
              //alert('hi');
              window.open($(this).parent().attr('youtubeurl'));
            });
              //$('#video_container').append('<iframe src="https://www.youtube.com/embed/8IBNZ6O2kMk"></iframe>');
        });
    </script>
    </head>
'''    
body='''
    <body>
        <header>
            My Favourite Movie Trailers
        </header>
    
    <div id="video_container" class="screen">
    </div>
    <section id="movies">
        {maincontent}
    </section>
    </body>
</html>
'''

main_content='''
<div class="images">
<figure id="trail" youtubeurl="{video_url}" width="200" height="200">
        <img src="{movieimage}" alt="{moviename}"/>
        <figcaption>
            {moviedescription}
        </figcaption>
</figure>
</div>
'''

def make_website(movies):
    output_file=open("index.html","w");
    content=''
    for movie in movies:
        content=content+main_content.format(movieimage=movie.poster_image_url,moviename=movie.title,moviedescription=movie.storyline,video_url=movie.trailer);
    output_file.write(html+body.format(maincontent=content));
    path=os.getcwd();
    path=path+"/index.html"
    print path
    webbrowser.open(path,new=1,autoraise=True)
    
#make_website();