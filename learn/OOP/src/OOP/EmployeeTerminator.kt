package OOP


interface EmployeeTerminatorView {
    fun enableTerminate(enable: Boolean)
    fun setEmployeeList(employees: List<String>)
    fun clearSelection()
}

class EmployeeTerminatorDialog : EmployeeTerminatorView {

    private lateinit var controller: EmployeeTerminatorController
    private lateinit var employees: List<String>

    fun initialize(controller: EmployeeTerminatorController) {
        this.controller = controller
    }

    override fun enableTerminate(enable: Boolean) {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }

    override fun setEmployeeList(employees: List<String>) {
        this.employees = employees
    }

    override fun clearSelection() {
        TODO("not implemented") //To change body of created functions use File | Settings | File Templates.
    }
}

interface EmployeeTerminatorController {
    fun selectionChanged(employee: String?)
    fun terminate()
}

class EmployeeTerminatorModel : EmployeeTerminatorController {

    private lateinit var view: EmployeeTerminatorView
    private lateinit var employees: MutableList<String>
    private var selectedEmployee: String? = null

    fun initialize(view: EmployeeTerminatorView, employees: List<String>) {
        this.view = view
        this.employees = employees as MutableList<String>
        view.setEmployeeList(this.employees)
        view.clearSelection()
        view.enableTerminate(false)
    }

    override fun selectionChanged(employee: String?) {
        view.enableTerminate(employee != null)
        selectedEmployee = employee
    }

    override fun terminate() {
        if (selectedEmployee != null) {
            employees.remove(selectedEmployee as String)
        }
        view.setEmployeeList(employees)
        view.clearSelection()
        view.enableTerminate(false)
    }
}