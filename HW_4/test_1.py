from flask import Flask, request
from mehanic import *
app = Flask(__name__)




@app.route('/get_all_time_track')
def get_all_time_track_route():
    days, hours, minutes, seconds = get_all_time_track()
    return f'Total duration of all tracks: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

@app.route('/get_all_info_about_track')
def get_all_info_about_track_route():
    track_id = request.args.get('TrackId')
    if track_id:
        track_info = get_all_info_about_track(track_id)
        if track_info:
            return f'''
                Track Name: {track_info[0]}<br>
                Album Title: {track_info[1]}<br>
                Artist Name: {track_info[2]}<br>
                Genre: {track_info[3]}<br>
                Composer: {track_info[4]}<br>
                Duration (ms): {track_info[5]}<br>
                Size (bytes): {track_info[6]}<br>
                Price: {track_info[7]}
            '''
        else:
            return 'Track not found', 404
    else:
        return 'TrackId not specified', 400


@app.route('/order_price')
def order_price():
    country = request.args.get('country')
    if country:
        total_sales = get_total_sales(country)
        return f'Total sales in {country}: {total_sales}'
    else:
        return 'Country not specified', 400

if __name__ == '__main__':
    app.run(debug=True)