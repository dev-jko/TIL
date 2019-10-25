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

//let number = "2"
//if let converted = Int(number) {
//    print(converted)
//} else {
//    print("else")
//}

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



for i in 0..<100 {
    i
}


var name:String = "Jaedoo Ko"
let birthyear:Int = 1993
name = "고재두"

"\(birthyear)에 태어난 \(name)"

var languages:[String] = ["swift", "kotlin"]
var capitals:[String:String] = [
    "한국":"서울",
    "일본":"도쿄"
]

languages[1]
capitals["한국"]

var languages2:[String] = []
var capitals2:[String:String] = [:]

var languages3 = [String]()
var capitals3 = [String:String]()

var age = 19
var student = ""

if age >= 8 && age < 14 {
    student = "초등학생"
} else if age < 17 {
    student = "중학생"
} else{
    student = "고등학생"
}

var number = 0
if number == 0 {
    
}

if name.isEmpty {
    
}

if languages.isEmpty {
    
}

switch age {
case 8..<14:
    student = "1"
case 14..<17:
    student = "2"
default:
    student = "기타"
}


for language in languages {
    print("저는 \(language) 언어를 다룰 수 있습니다.")
}

var ii = 0
while ii < 100 {
    ii += 1
}

var email:String?
print(email)

email = "email"
print(email)

let optionalEmail:String? = "email"
let requiredEmail:String = optionalEmail!

if let email = optionalEmail {
    print(email)
}
let optionalName:String? = "kjd"

if let name = optionalName,
    let email = optionalEmail {
    print("\(name), \(email)")
}

var optionalAge:Int? = 27

if let age = optionalAge, age > 20 {
    print(age)
}

let array:[String]? = []
var isEmptyArray = false

if let array = array, array.isEmpty {
    isEmptyArray = true
} else {
    isEmptyArray = false
}

let isEmptyArray2 = array?.isEmpty == true

print(isEmptyArray2)

//optionalEmail = nil
//print(optionalEmail!)

func hello(name:String, time:Int) -> String {
    var string = ""
    for _ in 0..<time {
        string += "\(name)님 안녕하세요 \n"
    }
    return string
}

hello(name: "고재두", time: 3)

func hello2(to name: String, numberOfTimes time: Int){
    for _ in 0..<time {
        print(name)
    }
}

hello2(to: "kjd", numberOfTimes: 3)

func hello3(_ name: String, time: Int = 2){
    print(name)
    print(time)
}


hello3("name", time: 3)
hello3("name2")


func sum(_ numbers: Int...) -> Int {
    var sum = 0
    for number in numbers {
        sum += number
    }
    return sum
}

sum(1, 2)
sum(1,2,3)


func hello4(name:String, time:Int){
    func message(name:String) -> String {
        return "\(name) hello"
    }
    
    for _ in 0 ..< time {
        print(message(name: name))
    }
}

hello4(name: "hi", time: 3)

func helloGenerator(message:String) -> (String, String) -> String {
    return { (first:String, last:String) -> String in
        return first + last
    }
}

print(helloGenerator(message: "hello")("Jaedoo", "Ko"))

func helloGenerator2(message:String) -> (String, String) -> String {
    return { first, last in
        return first + last
    }
}

func helloGenerator3(message:String) -> (String, String) -> String {
    return {
        return $1 + $0
    }
}

func helloGenerator4(message:String) -> (String, String) -> String {
    return { $1 + $0 }
}

let numberArr12 = [10, 2, 9, 3, 4, 5, 6]
let sortedNumbers:[Int] = numberArr12.sorted { $0 < $1 }
print(sortedNumbers)

let evens = numberArr12.filter { $0 % 2 == 0 }
print(evens)

print(numberArr12.map { $0 * 2 })

print(numberArr12.reduce(0) { $0 + $1 })
print(numberArr12.reduce(0, +)) // 연산자도 함수다

class Dog {
    var name:String?
    var age:Int?
    
    func description() -> String {
        if let name = self.name {
            return "dog \(name)"
        } else {
            return "no name"
        }
    }
}

struct Coffee {
    var name:String?
    var size:String?
    
    func description() -> String {
        if let name = self.name {
            return "coffee \(name)"
        } else {
            return "no name"
        }
    }
}

var myDog = Dog()
myDog.name = "찡코"
myDog.age = 3
print(myDog.description())

var myCoffee = Coffee()
myCoffee.name = "아메리카노"
myCoffee.size = "venti"
print(myCoffee.description())

let my = Dog()
my.name = "dfdf"
print(my.description())

class Animal {
    let numberOfLegs = 4
}

class Dog2:Animal {
    var name:String?
    var age:Int?
}

