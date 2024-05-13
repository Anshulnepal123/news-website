let quote = document.querySelector('.quote');


const quotes = () => {
  let obj = {
    "Edward Bulwer-Lytton": "The pen is mightier than the sword",
    "Frank Lloyd Wright": "The truth is more important than the facts.",
    "Winston Churchill": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Mark Twain": "The secret of getting ahead is getting started.",
    "Maya Angelou": "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
    "Albert Einstein": "Imagination is more important than knowledge.",
    "Oprah Winfrey": "The biggest adventure you can take is to live the life of your dreams.",
    "Nelson Mandela": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Helen Keller": "The only thing worse than being blind is having sight but no vision.",
    "Martin Luther King Jr.": "Faith is taking the first step even when you don't see the whole staircase."
  };
  let authors = Object.keys(obj);
  let author = authors[Math.floor(Math.random() * authors.length)];
  let quoteText = obj[author];
  quote.innerHTML = `"${quoteText}" - ${author}`;
};

quotes(); // Call the function to display a random quote when the page loads


