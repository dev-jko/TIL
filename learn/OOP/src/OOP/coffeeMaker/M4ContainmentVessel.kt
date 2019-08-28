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

    }

    private fun handleBrewingEvent(potStatus: Int) {
        when (potStatus) {
            CoffeeMakerAPI.POT_NOT_EMPTY -> {
                containerAvailable()
                api.setWarmerState(CoffeeMakerAPI.WARMER_ON)
            }
            CoffeeMakerAPI.WARMER_EMPTY -> {
                containerUnavailable()
                api.setWarmerState(CoffeeMakerAPI.WARMER_OFF)
            }
            else -> {
                containerAvailable()
                api.setWarmerState(CoffeeMakerAPI.WARMER_OFF)
            }
        }
    }
}