let person = {
    name: 'Sikato',
    age: 45,
    city: 'Pernik'
};

let {name, ...rest} = person;

console.log(rest);