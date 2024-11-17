from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 7,
        "location": "Makati",
        "restaurant_name": "Restaurant Seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/776538/pexels-photo-776538.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 8,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Eight",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1581554/pexels-photo-1581554.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 9,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1449773/pexels-photo-1449773.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 10,
        "location": "Pasig",
        "restaurant_name": "Restaurant Ten",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/460537/pexels-photo-460537.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 11,
        "location": "Taguig",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2290753/pexels-photo-2290753.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 12,
        "location": "Laguna",
        "restaurant_name": "Restaurant Twelve",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/1055058/pexels-photo-1055058.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 13,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1237073/pexels-photo-1237073.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 14,
        "location": "Marikina",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2788792/pexels-photo-2788792.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 15,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/984888/pexels-photo-984888.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 16,
        "location": "Cavite",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/6267/menu-restaurant-vintage-table.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 17,
        "location": "Pasig",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2290070/pexels-photo-2290070.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 18,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/3201921/pexels-photo-3201921.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 19,
        "location": "Makati",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/4450334/pexels-photo-4450334.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 20,
        "location": "Marikina",
        "restaurant_name": "Restaurant Twenty",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/1438445/pexels-photo-1438445.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 21,
        "location": "Taguig",
        "restaurant_name": "Restaurant Twenty-one",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2067576/pexels-photo-2067576.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 22,
        "location": "Cavite",
        "restaurant_name": "Restaurant Twenty-two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1055054/pexels-photo-1055054.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 23,
        "location": "Tarlac",
        "restaurant_name": "Restaurant Twenty-three",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/110813/pexels-photo-110813.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 24,
        "location": "Taguig",
        "restaurant_name": "Restaurant Twenty-four",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/1833320/pexels-photo-1833320.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 25,
        "location": "Marikina",
        "restaurant_name": "Restaurant Twenty-five",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/418806/pexels-photo-418806.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 26,
        "location": "Pampanga",
        "restaurant_name": "Restaurant Twenty-six",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/1579715/pexels-photo-1579715.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 27,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Twenty-seven",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/887723/pexels-photo-887723.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 28,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Twenty-eight",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2923034/pexels-photo-2923034.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 29,
        "location": "Makati",
        "restaurant_name": "Restaurant Twenty-nine",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/390658/pexels-photo-390658.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 30,
        "location": "Marikina",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2894275/pexels-photo-2894275.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 31,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Thirty-one",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/2067560/pexels-photo-2067560.jpeg?auto=compress&cs=tinysrgb&w=600"
    }, {
        "id": 32,
        "location": "Laguna",
        "restaurant_name": "Restaurant Thirty-two",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/1121480/pexels-photo-1121480.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 33,
        "location": "Pampanga",
        "restaurant_name": "Restaurant Thirty-three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5865304/pexels-photo-5865304.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 34,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Thirty-four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/34650/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 35,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Thirty-five",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/5490933/pexels-photo-5490933.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 36,
        "location": "Tarlac",
        "restaurant_name": "Restaurant Thirty-six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/4309/city-restaurant-table-pavement.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 37,
        "location": "Pasig",
        "restaurant_name": "Restaurant Thirty-seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2956952/pexels-photo-2956952.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 38,
        "location": "Alabang",
        "restaurant_name": "Restaurant Thirty-eight",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/5865147/pexels-photo-5865147.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 39,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Thirty-nine",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2728186/pexels-photo-2728186.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 40,
        "location": "Taguig",
        "restaurant_name": "Restaurant Fourty",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2193600/pexels-photo-2193600.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 41,
        "location": "Laguna",
        "restaurant_name": "Restaurant Fourty-one",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2092059/pexels-photo-2092059.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 42,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Fourty-two",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2813132/pexels-photo-2813132.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 43,
        "location": "Taguig",
        "restaurant_name": "Restaurant Fourty-three",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/756086/pexels-photo-756086.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 44,
        "location": "Pasig",
        "restaurant_name": "Restaurant Fourty-four",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2530586/pexels-photo-2530586.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 45,
        "location": "Marikina",
        "restaurant_name": "Restaurant Fourty-five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2612334/pexels-photo-2612334.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 46,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Fourty-six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/5531434/pexels-photo-5531434.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 47,
        "location": "Pampanga",
        "restaurant_name": "Restaurant Fourty-seven",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2566038/pexels-photo-2566038.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 48,
        "location": "Taguig",
        "restaurant_name": "Restaurant Fourty-eight",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/3690255/pexels-photo-3690255.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 49,
        "location": "Taguig",
        "restaurant_name": "Restaurant Fourty-nine",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/2504980/pexels-photo-2504980.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 50,
        "location": "Taguig",
        "restaurant_name": "Restaurant Fifty",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/29420328/pexels-photo-29420328/free-photo-of-cozy-greenhouse-cafe-in-hudson-ny.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
]



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)