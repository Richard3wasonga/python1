const [num1,num2] =[200,125]

console.log(num1)

if(num1 < num2){
    console.log(`sure ${num1} is less than ${num2}`)
}else if (num1 === num2){
    console.log(`sure ${num1} is equal to ${num2}`)
}else {
    console.log(`${num1} is greater than ${num2}`)
}

const sentence =`
This is a random sentence i have just written
`

if(sentence.includes('have')){
    console.log("The word have is seen in the sentence")
}