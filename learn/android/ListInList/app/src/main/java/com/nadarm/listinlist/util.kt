package com.nadarm.listinlist

import android.view.View
import androidx.databinding.BindingAdapter
import com.nadarm.listinlist.ui.MainItem
import com.nadarm.listinlist.ui.MainListAdapter


@BindingAdapter(value = ["newList", "listAdapter"], requireAll = true)
fun bindList(view: View, newList: List<MainItem>, listAdapter: MainListAdapter) {
    listAdapter.submitList(newList)
}