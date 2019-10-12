import UIKit

var str = "Hello, playground"
print(str)

let s = "Hello World!"
s.uppercased()
let t = Array(s)
print(t)


let i = true
if i {
    print("if")
} else {
    print("else")
}


let httpsResponse = (status:200, msg:"ok")
print(httpsResponse.status, httpsResponse.msg)
print(httpsResponse.0, httpsResponse.1)

let number = "2"
if let converted = Int(number) {
    print(converted)
} else {
    print("else")
}

var myNum = 0
let timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true){_ in
    myNum += 1
    print(myNum)
}

timer.invalidate()

//while true {
//    if myNum == 5 {
//        timer.invalidate()
//    }
//    print("while \(myNum)")
//}

