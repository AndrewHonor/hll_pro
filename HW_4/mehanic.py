import sqlite3
from functools import wraps

def execute_query(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('chinook.db')
        try:
            result = func(connection, *args, **kwargs)
        finally:
            connection.close()
        return result
    return wrapper



@execute_query
def get_total_sales(connection, country):
    cursor = connection.cursor()
    cursor.execute('SELECT SUM(Total) FROM invoices WHERE BillingCountry = ?', (country,))
    total_sales = cursor.fetchone()[0]
    return total_sales

@execute_query
def get_all_info_about_track(connection, track_id):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT tracks.Name, albums.Title, artists.Name, genres.Name, tracks.Composer, tracks.Milliseconds, tracks.Bytes, tracks.UnitPrice
        FROM tracks
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        JOIN genres ON tracks.GenreId = genres.GenreId
        WHERE tracks.TrackId = ?
    ''', (track_id,))
    track_info = cursor.fetchone()
    return track_info


@execute_query
def get_all_time_track(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT SUM(Milliseconds) FROM tracks')
    total_duration_ms = cursor.fetchone()[0]
    total_seconds = total_duration_ms // 1000
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return days, hours, minutes, seconds
