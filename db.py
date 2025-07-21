users: dict[int, dict[str, bool]] = {}


emojiConditions={
    1000:{
        'day':'☀️',
        'night':'🌙'
    },
    1003:{
        'day':'⛅',
        'night':'☁️'
    },
    1006:{
        'day':'☁️',
        'night':'☁️'
    },
    1009:{
        'day':'☁️',
        'night':'☁️'
    },
    1030:{  # Fixed typo: was 10030
        'day':'🌫️',
        'night':'🌫️'
    },
    1063:{
        'day':'🌦️',
        'night':'🌧️'
    },
    1066:{
        'day':'❄️',
        'night':'❄️'
    },
    1069:{
        'day':'🌨️',
        'night':'🌨️'
    },
    1072:{
        'day':'🧊',
        'night':'🧊'
    },
    1087:{
        'day':'⛈️',
        'night':'⛈️'
    },
    1114:{
        'day':'🌨️',
        'night':'🌨️'
    },
    1117:{
        'day':'🌨️',
        'night':'🌨️'
    },
    1135:{
        'day':'🌫️',
        'night':'🌫️'
    },
    1147:{
        'day':'🌫️',
        'night':'🌫️'
    },
    1150:{
        'day':'💧',
        'night':'💧'
    },
    1153:{
        'day':'💧',
        'night':'💧'
    },
    1168:{
        'day':'🧊',
        'night':'🧊'
    },
    1171:{
        'day':'🧊',
        'night':'🧊'
    },
    1180:{
        'day':'🌦️',
        'night':'🌧️'
    },
    1183:{
        'day':'🌧️',
        'night':'🌧️'
    },
    1186:{
        'day':'🌦️',
        'night':'🌧️'
    },
    1189:{
        'day':'🌧️',
        'night':'🌧️'
    },
    1192:{
        'day':'☔',
        'night':'☔'
    },
    1195:{
        'day':'☔',
        'night':'☔'
    },
    1198:{  # Light freezing rain
        'day':'🧊',
        'night':'🧊'
    },
    1201:{  # Moderate or heavy freezing rain
        'day':'🧊',
        'night':'🧊'
    },
    1204:{  # Light sleet
        'day':'🌨️',
        'night':'🌨️'
    },
    1207:{  # Moderate or heavy sleet
        'day':'🌨️',
        'night':'🌨️'
    },
    1210:{  # Patchy light snow
        'day':'❄️',
        'night':'❄️'
    },
    1213:{  # Light snow
        'day':'❄️',
        'night':'❄️'
    },
    1216:{  # Patchy moderate snow
        'day':'🌨️',
        'night':'🌨️'
    },
    1219:{  # Moderate snow
        'day':'🌨️',
        'night':'🌨️'
    },
    1222:{  # Patchy heavy snow
        'day':'🌨️',
        'night':'🌨️'
    },
    1225:{  # Heavy snow
        'day':'🌨️',
        'night':'🌨️'
    },
    1237:{  # Ice pellets
        'day':'🧊',
        'night':'🧊'
    },
    1240:{  # Light rain shower
        'day':'🌦️',
        'night':'🌧️'
    },
    1243:{  # Moderate or heavy rain shower
        'day':'🌧️',
        'night':'🌧️'
    },
    1246:{  # Torrential rain shower
        'day':'☔',
        'night':'☔'
    },
    1249:{  # Light sleet showers
        'day':'🌨️',
        'night':'🌨️'
    },
    1252:{  # Moderate or heavy sleet showers
        'day':'🌨️',
        'night':'🌨️'
    },
    1255:{  # Light snow showers
        'day':'❄️',
        'night':'❄️'
    },
    1258:{  # Moderate or heavy snow showers
        'day':'🌨️',
        'night':'🌨️'
    },
    1261:{  # Light showers of ice pellets
        'day':'🧊',
        'night':'🧊'
    },
    1264:{  # Moderate or heavy showers of ice pellets
        'day':'🧊',
        'night':'🧊'
    },
    1273:{  # Patchy light rain with thunder
        'day':'⛈️',
        'night':'⛈️'
    },
    1276:{  # Moderate or heavy rain with thunder
        'day':'⛈️',
        'night':'⛈️'
    },
    1279:{  # Patchy light snow with thunder
        'day':'⛈️',
        'night':'⛈️'
    },
    1282:{  # Moderate or heavy snow with thunder
        'day':'⛈️',
        'night':'⛈️'
    }
}