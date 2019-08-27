package OOP.coffeeMaker

abstract class HotWaterSource {
    private lateinit var ui: UserInterface
    private lateinit var cv: ContainmentVessel
    protected var isBrewing: Boolean = false

    fun init(ui: UserInterface, cv: ContainmentVessel) {
        this.ui = ui
        this.cv = cv
    }

    fun start() {
        isBrewing = true
        startBrewing()
    }

    fun done(){
        isBrewing = false
    }

    protected fun declareDone(){
        ui.done()
        cv.done()
        isBrewing = false
    }

    abstract fun startBrewing()
    abstract fun isReady(): Boolean
    abstract fun pause()
    abstract fun resume()
}
