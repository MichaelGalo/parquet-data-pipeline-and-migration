use('Lab_One_10');

// Example list of car objects
const cars = [
  { make: "Toyota", model: "Corolla", year: 2020 },
  { make: "Honda", model: "Civic", year: 2019 },
  { make: "Ford", model: "Mustang", year: 2021 }
];

// Insert the list into the 'cars' collection
db.cars.insertMany(cars);