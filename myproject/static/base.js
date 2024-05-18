/*
// Create a new Date object
const currentDate = new Date();

// Get the year
const year = currentDate.getFullYear();

// Get the month (returns a value between 0 and 11, where 0 corresponds to January)
const month = currentDate.getMonth() + 1; // Adding 1 to get the actual month number

// Get the day of the month
const day = currentDate.getDate();

// Get the hour (in 24-hour format)
const hour = currentDate.getHours();

// Get the minutes
const minutes = currentDate.getMinutes();

// Get the seconds
const seconds = currentDate.getSeconds();

// Get the milliseconds
const milliseconds = currentDate.getMilliseconds();

// Output the results
console.log(`Year: ${year}`);
console.log(`Month: ${month}`);
console.log(`Day: ${day}`);
console.log(`Hour: ${hour}`);
console.log(`Minutes: ${minutes}`);
console.log(`Seconds: ${seconds}`);
console.log(`Milliseconds: ${milliseconds}`);
*/

// Select the element with class 'date'
let dates = document.querySelector('.date');

// Create a new Date object
let current_date = new Date();

// Define arrays for day of week and month names
let dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
let monthOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

// Get the day, month, date, and year
let day = dayOfWeek[current_date.getDay()];
let month = monthOfYear[current_date.getMonth()];
let date = current_date.getDate();
let year = current_date.getFullYear();
//Get the hours, min, sec
// Update the innerHTML of the element with the formatted date
dates.innerHTML = `${day}, ${month} ${date}, ${year}`;




//Step1:this code will execute first it will send the city name to weather after that
const getWeather = () => {
    const cityName = document.getElementById('city-name').value;
    weather(cityName)
};


//weather update
//step2 :weather will recive the city name and and put it in the api which gives all the information 
//about that particular palce
const weather = (city ='kathmandu') => {
    const apikey = '7d9f6c3259a413336f3e08c98031193e';
    let we = document.querySelector('.weather');
    const currentWeatherUrl = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apikey}`;
    fetch(currentWeatherUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
           displayweather(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

};
weather();


//step3:After receiving the data it will display the data in the webpage
const displayweather = (data)=>{
    const weatherElement = document.querySelector('.weather');
    const weatherdetail = document.querySelector('.weatherdetails');
    const iconCode = data.weather[0].icon;
    const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@4x.png`
    const tempinc = data.main.temp - 273.15
// Assuming the structure of the weather data is like: { temperature: 20, description: "Sunny" }
    weatherElement.innerHTML= ` <img src="/static/sun.png" alt="img" class="sun">${tempinc.toFixed(2)}°C, ${data.name}`
    weatherdetail.innerHTML =  `<p>City: ${data.name}</p>
    <p>Temperature: ${(data.main.temp - 273.15).toFixed(2)}°C</p>
    <p>Description: ${data.weather[0].description}</p>
    <p>Humidity: ${data.main.humidity}%</p>
    <p>Wind Speed: ${data.wind.speed} m/s</p>
    <p>Pressure: ${data.main.pressure} hPa</p>`

}

/*modal*/
let modal = document.querySelector('.modal')
let climate = () =>{
    modal.style.display = 'block';
}
let closed = ()=>{
    modal.style.display = 'none'
}
