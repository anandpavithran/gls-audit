# Welcome to GLS Audit Facility



### Read the instructions
<html>
1. Download the iso. 

  <body>
    <button onclick="window.location.href='https://www.redhat.com';">
      Download
    </button>
  </body>
  <br>

2. Create a bootable USB stick.
  
  <body>
    <button onclick="window.location.href='https://www.redhat.com';">
      Steps
    </button>
  </body>
  <br>

3. Fetch the Hardware information.

  <body>
    <button onclick="window.location.href='https://www.redhat.com';">
      Fetch
    </button>
  </body>
  <br>
  var http = require("http");

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});
  for (i=10;i>0;i--){
      response.write(String(i)+"<br />");
  }
  response.end('Boom!!!');
}).listen(8081);

console.log('Server running at http://127.0.0.1:8081/');
  
  
  
</html>
