// 1491. Average Salary Excluding the Minimum and Maximum Salary

// Solution 1
var average = function(salary) {
    let sum = 0;
    salary.sort((a, b) => {return a - b});
    for (let i = 1; i < salary.length - 1; i++){
        sum += salary[i];
    }
    return sum / (salary.length - 2);
};


// Solution 2
var average = function(salary) {
    return ((salary.reduce((x, y) =>x + y) - Math.max(...salary) - Math.min(...salary)) / (salary.length - 2))
};