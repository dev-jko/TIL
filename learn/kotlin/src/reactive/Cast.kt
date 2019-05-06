package reactive

import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val list = listOf<MyItemInherit>(
            MyItemInherit(1),
            MyItemInherit(2),
            MyItemInherit(3),
            MyItemInherit(4),
            MyItemInherit(5),
            MyItemInherit(6),
            MyItemInherit(7)
    )

    list.toObservable().map { it as MyCastItem }
            .subscribe { println(it) }

    list.toObservable().cast(MyCastItem::class.java)
            .subscribe { println(it) }

}

open class MyCastItem(val id: Int) {
    override fun toString(): String {
        return "[MyItem $id]"
    }
}

class MyItemInherit(id: Int) : MyCastItem(id) {
    override fun toString(): String {
        return "[MyItemInherit $id]"
    }
}
