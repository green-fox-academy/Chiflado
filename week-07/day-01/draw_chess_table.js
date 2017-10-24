// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//
field = ''

for (let i = 1; i < 9; i += 1){
    if (i % 2 === 0){
        for (let j = 1; j < 9;j += 1){
            if (j % 2 === 0){
                field += '%';
            } else{
                field += ' ';
            }
        }
    }else{
        for (let j = 1; j < 9;j += 1){
            if (j % 2 === 0){
                field += ' ';
            } else{
                field += '%';
            }
        }
    }
    console.log(field);
    field = '';    
}