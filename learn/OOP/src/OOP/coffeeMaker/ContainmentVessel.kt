package OOP.coffeeMaker

abstract class ContainmentVessel {
    private lateinit var ui: UserInterface
    private lateinit var hotWaterSource: HotWaterSource
    protected var isBrewing: Boolean = false
    protected var isComplete: Boolean = true

    fun init(ui: UserInterface, hotWaterSource: HotWaterSource) {
        this.ui = ui
        this.hotWaterSource = hotWaterSource
    }

    fun start() {
        isBrewing = true
        isComplete = false
    }

    fun done() {
        isBrewing = false
    }

    protected fun declareComplete() {
        ui.complete()
        isComplete = true
    }

    protected fun containerAvailable() {
        hotWaterSource.resume()
    }

    protected fun containerUnavailable() {
        hotWaterSource.pause()
    }

    abstract fun isReady(): Boolean
}
