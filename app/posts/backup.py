@posts.route('/create', methods = ['POST', 'GET'])
def create_post():

    if request.method =='POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title = title, body = body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Error: something wrong')

        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form = form)