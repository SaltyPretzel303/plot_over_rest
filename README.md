# plot_over_rest
rest api for adding points and ploting them.  
start server using: `$ python server.py`  
`[post] .../add     -> expects data in json format: {x:10, y:200}, adds point to the array which will be ploted`  
`[get]  .../clear   -> will clear array of (previously added) points`  
`[get]  .../print   -> will plot currently available points and return .png image`  
