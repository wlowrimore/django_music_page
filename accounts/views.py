





# def profile(request, username):
#     if request.method == 'POST':
#         user = request.user
#         form = UserUpdateForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             user_form = form.save()
#
#             messages.success(request, f'{user_form}, Your profile has been updated!')
#             return redirect('profile', user_form.username)
#
#         for error in list(form.errors.values()):
#             messages.error(request, error)
#
#     user = get_user_model().objects.filter(username=username).first()
#     if user:
#         form = UserUpdateForm(instance=user)
#         form.fields['description'].widget.attrs = {
#             'class': 'bg-gray-200 p-2 text-light text-sm tracking-wide rounded-sm', 'rows': 10, 'max_length': 255}
#         form.fields['first_name'].widget.attrs = {
#             'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
#         form.fields['last_name'].widget.attrs = {
#             'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
#         form.fields['email'].widget.attrs = {
#             'class': 'bg-gray-200 py-1 px-2 text-light text-sm tracking-wide rounded-sm'}
#         context = {'form': form}
#         return render(request, 'accounts/profile.html', context)
#
#     return redirect('home')


