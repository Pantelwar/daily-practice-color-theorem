var areas = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9"]
var colors = ["G", "Y", "B", "O"]
var adjacentAreas = [
    ["A4", "A1"], ["A4", "A2"], ["A4", "A7"], ["A4", "A5"],
    ["A4", "A3"], ["A4", "A6"],
    ["A1", "A2"], ["A1", "A6"],
    ["A5", "A6"], ["A5", "A3"],
    ["A3", "A7"], ["A3", "A2"],
    ["A2", "A7"], ["A2", "A6"],
    ["A8", "A2"], ["A8", "A3"],
    ["A9", "A5"], ["A9", "A6"], ["A9", "A2"], ["A9", "A8"]
]

//Initialize colors assigned object
var colorsAssigned = {}

//Assign every area with the colors array
for (a = 0; a < areas.length; a++) {
    colorsAssigned[areas[a]] = colors;
}

//Loop over the areas array
for (let a = 0; a < areas.length; a++) {
    //Loop over the adjacentAreas array 
    for (i = 0; i < adjacentAreas.length; i++) {
        /*
            check whether the area we're searching matches the first element of the array and then
            pop out color assigned to it from the adjacent areas' colors array.
        */
        if (adjacentAreas[i][0] == areas[a]) {
            let color = [...colorsAssigned[adjacentAreas[i][1]]]
            var index = color.indexOf(colorsAssigned[adjacentAreas[i][0]][0]);
            if (index > -1) {
                color.splice(index, 1)
            }
            colorsAssigned[adjacentAreas[i][1]] = color
        }
        /*
            check whether the area we're searching matches the second element of the array and then
            pop out color assigned to it from the adjacent areas' colors array.
        */
        if (adjacentAreas[i][1] == areas[a]) {
            let color = [...colorsAssigned[adjacentAreas[i][0]]]
            var index = color.indexOf(colorsAssigned[adjacentAreas[i][1]][0]);
            if (index > -1) {
                color.splice(index, 1)
            }
            colorsAssigned[adjacentAreas[i][0]] = color
        }
    }
}

//Pick the first color from the array
Object.keys(colorsAssigned).forEach(function (key) {
    colorsAssigned[key] = colorsAssigned[key][0]
})
console.log("result", colorsAssigned)