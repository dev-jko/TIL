fun main(args: Array<String>) {
    println("hello world")
    val a: Int = 2
    val b = 1
    val c: Int = 3
    println(a + b)
    var d: Int = 2
    d = 1
    println(d)
    println(myFunc(a, b))
    val a_nullable: Int? = null
    println(a_nullable)


    val myList = ArrayList<String>()
    myList.add("1")
    myList.add("2")
    myList.add("3")
    for (s in myList){
        println("data : $s")
        when (s){
            "1" -> println("$s 입니다")
            is String -> println("String 입니다")
            else -> println("String 아닙니다")
        }
    }

    for (x in 1..5) {
        println(x)
    }

}

fun myFunc(a: Int, b: Int): Int {
    return a + b
}

