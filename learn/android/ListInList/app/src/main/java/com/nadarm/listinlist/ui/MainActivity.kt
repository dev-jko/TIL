package com.nadarm.listinlist.ui

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.ListAdapter
import com.nadarm.listinlist.Callback
import com.nadarm.listinlist.R
import com.nadarm.listinlist.data.ArticleDao
import com.nadarm.listinlist.databinding.ActivityMainBinding
import dagger.android.AndroidInjection
import javax.inject.Inject


class MainActivity : AppCompatActivity(), Callback {

    private val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
    }
    private val mainAdapter: ListAdapter<MainItem, ViewHolder> = MainListAdapter(this)

    @Inject
    lateinit var dao: ArticleDao

    override fun onCreate(savedInstanceState: Bundle?) {

        AndroidInjection.inject(this)

        super.onCreate(savedInstanceState)

        println(dao.getArticle(0))

        binding.mainRecyclerView.adapter = mainAdapter

//        mainAdapter.submitList(getListInList())
    }


//    private fun getListInList(): List<MainItem> {
//        val result = ArrayList<MainItem>()
//        result.add(MainItem.HeaderItem("인기"))
//        val temp: MainItem =
//            MainItem.ArticlesItem(manager.articles.map { MainItem.ArticlePreviewItem(it) })
//        result.add(temp)
//        result.add(MainItem.HeaderItem("목록"))
//        manager.articles.forEach {
//            val item = MainItem.ArticleItem(it)
//            result.add(item)
//        }
//        return result
//    }

    override fun callback(item: MainItem) {
        Toast.makeText(this, "item : ${item.getItem()}", Toast.LENGTH_SHORT).show()
    }
}
