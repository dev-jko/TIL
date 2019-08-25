package designPatterns

fun main() {
    val oldPhone = OldPhone()
    chargePhone(oldPhone)

    val adapter = Adapter()
    val newPhone = NewPhone()
    adapter.phone = newPhone
    chargePhone(adapter)
}

fun chargePhone(connectable: Connectable) {
    connectable.plug220v()
}

interface Connectable {
    fun plug220v()
}

class OldPhone : Connectable {
    override fun plug220v() {
        println("old phone charge 220v")
    }
}

class NewPhone {
    fun charge() {
        println("new phone charge")
    }
}

class Adapter(
    var phone: NewPhone?
) : Connectable {

    constructor() : this(null)

    override fun plug220v() {
        phone?.charge()
    }
}
