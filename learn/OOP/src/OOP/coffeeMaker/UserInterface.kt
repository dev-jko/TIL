package OOP.coffeeMaker

abstract class UserInterface {
    private lateinit var hotWaterSource: HotWaterSource
    private lateinit var containmentVessel: ContainmentVessel
    protected var isComplete: Boolean = false

    fun init(hws: HotWaterSource, cv: ContainmentVessel) {
        hotWaterSource = hws
        containmentVessel = cv
    }

    fun complete() {
        isComplete = true
        completeCycle()
    }

    protected fun startBrewing() {
        if (hotWaterSource.isReady() && containmentVessel.isReady()) {
            isComplete = false
            hotWaterSource.start()
            containmentVessel.start()
        }
    }

    abstract fun done()
    abstract fun completeCycle()
}