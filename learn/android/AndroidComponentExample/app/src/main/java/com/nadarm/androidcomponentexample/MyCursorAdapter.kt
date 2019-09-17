package com.nadarm.androidcomponentexample

import android.content.Context
import android.database.Cursor
import android.net.Uri
import android.provider.MediaStore
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.CursorAdapter
import android.widget.ImageView

class MyCursorAdapter(
    context: Context, c: Cursor?
) : CursorAdapter(context, c, false) {

    override fun newView(context: Context, cursor: Cursor?, parent: ViewGroup): View {
        val inflater = LayoutInflater.from(context)
        return inflater.inflate(R.layout.item_photo, parent, false)
    }

    override fun bindView(view: View, context: Context, cursor: Cursor?) {
        val imageView: ImageView = view.findViewById(R.id.photo_image)
        if (cursor != null) {
            val uri = cursor.getString(cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA))
            imageView.setImageURI(Uri.parse(uri))
        }
    }
}