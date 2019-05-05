package reactive

import io.reactivex.Flowable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>) {
    Flowable.range(1, 300).map { MyItem(it) }.observeOn(Schedulers.computation())
            .subscribe({
                println("Received $it")
                runBlocking { delay(50) }
            }, { it.printStackTrace() })
    runBlocking { delay(20000) }
}

data class MyItem(val id: Int) {
    init {
        println("MyItem Created $id")
    }
}
