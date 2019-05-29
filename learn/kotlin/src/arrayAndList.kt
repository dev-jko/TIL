
fun main() {
    val array: Array<Int> = arrayOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    val list: List<Int> = listOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    val mutableList: MutableList<Int> = mutableListOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    println(array.joinToString(prefix = "array item : "))
    println(list.joinToString(prefix = "list item : "))
    println(mutableList.joinToString(prefix = "mutableList item : "))

    array[0] = -1
//    list[0] = -1 // list는 변경 불가
    mutableList[0] = -1

    println(array.joinToString(prefix = "array item : "))
    println(list.joinToString(prefix = "list item : "))
    println(mutableList.joinToString(prefix = "mutableList item : "))
}

