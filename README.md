# PingPongOpenCV
Python project to take a rtmp stream from a ping pong table and see if serves are onsides.

We have an instance of Nginx with RTMP module running on a raspberry pi.  The pi has the camera module and uses ffmpeg to push the stream to Nginx RTMP instance.  Our OpenCV code will then consume the stream and process the lines and balls and push the processed stream to the Nginx instance. 
