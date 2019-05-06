import io.reactivex.Flowable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>) {
    val flowable = Flowable.generate<Int> {
        it.onNext(GenerateFlowableItem.item)
    }

    flowable.map { MyItemFlowable(it) }.observeOn(Schedulers.io())
            .subscribe {
                runBlocking { delay(25) }
                println("Next: $it")
            }

    runBlocking { delay(30000) }
}

data class MyItemFlowable(val id: Int) {
    init {
        println("MyItemFlowable Created $id")
    }
}

object GenerateFlowableItem {
    var item: Int = 0
        get() {
            return ++field
        }
}

