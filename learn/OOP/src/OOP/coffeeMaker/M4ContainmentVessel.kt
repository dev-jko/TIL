package OOP.coffeeMaker

class M4ContainmentVessel(
        private val api: CoffeeMakerAPI
) : ContainmentVessel(), Pollable {
    private var lastPotStatus: Int = CoffeeMakerAPI.POT_EMPTY

    override fun isReady(): Boolean {
        val plateStatus = api.getWarmerPlateStatus()
        return plateStatus == CoffeeMakerAPI.POT_EMPTY
    }

    override fun poll() {
        val potStatus = api.getWarmerPlateStatus()
        if (potStatus != lastPotStatus) {
            if (isBrewing) {
                handleBrewingEvent(potStatus)
            } else if (isComplete == false) {
                handleIncompleteEvent(potStatus)
            }
            lastPotStatus = potStatus
        }
    }

    private fun handleIncompleteEvent(potStatus: Int) {
        TODO()
    }

    private fun handleBrewingEvent(potStatus: Int) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }
}