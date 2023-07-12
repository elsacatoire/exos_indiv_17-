
/* elsa_des_bois
exercice individuel : performance des languages - version JavaScript */

/* Declaring things here */

// getiint time in miliseconds (int)
function now() { 
    const getNow = new Date
    return getNow.getTime()
}

function add(a, b) {
    return a + b
}

function add_array(array, number_to_add) {
    const newArray = array.map(x => x + number_to_add)
    return newArray
}

function fact(nbr) {
    if (nbr === 0)
    {
        return 1;
    }
  return nbr * fact(nbr-1);
}


/* We run things here */
// start
const initial_time = now()

// code to evaluate
const sum = add(3, 4)
console.log(sum);

const addedArrey = add_array([3, 4, 1, 10], 1)
console.log(addedArrey);

console.log(fact(5));

// code performance evaluation in milisecondes
const final_time = now()
const time_to_process = final_time - initial_time
console.log("L'éxécution à durée " + time_to_process + " miliseconds");