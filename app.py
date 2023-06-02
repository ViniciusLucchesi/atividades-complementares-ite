from robyn import Robyn
from robyn.robyn import Response
from scraper import main


app = Robyn(__file__)



@app.get('/api/activities/hours/asc')
async def activities_hours_asc(request):
    order = {'elements': 'hours', 'reverse': False}
    return Response(
        status_code = 200,
        headers = {"Content-Type": "application/json; charset=utf-8"}, 
        body = main(order)
    )

@app.get('/api/activities/hours/desc')
async def activities_hours_desc(request):
    order = {'elements': 'hours', 'reverse': True}
    return Response(
        status_code = 200,
        headers = {"Content-Type": "application/json; charset=utf-8"}, 
        body = main(order)
    )

@app.get('/api/activities/group/asc')
async def activities_group_asc(request):
    order = {'elements': 'group', 'reverse': False}
    return Response(
        status_code = 200,
        headers = {"Content-Type": "application/json; charset=utf-8"}, 
        body = main(order)
    )

@app.get('/api/activities/group/desc')
async def activities_group_asc(request):
    order = {'elements': 'group', 'reverse': True}
    return Response(
        status_code = 200,
        headers = {"Content-Type": "application/json; charset=utf-8"}, 
        body = main(order)
    )



if __name__ == '__main__':
    app.start(url="0.0.0.0", port=8080)