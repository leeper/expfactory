'''
views.py: part of expfactory package

Copyright (c) 2017, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

from flask import (
    flash,
    render_template, 
    redirect,
    session
)

from expfactory.logger import bot
import os


def perform_checks(template, do_redirect=False, context=None):
    '''return all checks for required variables before returning to 
       desired view
    '''
    from expfactory.server import app

    bot.debug('Performing checks...')
    username = session.get('username')
    subid = session.get('username')
    last = session.get('exp_id')
    next = app.get_next(session)
    session['exp_id'] = experiment

    if username is None:
        flash('You must start a session before doing experiments.')
        return redirect('/')

    if subid is None:
        flash('You must have a participant identifier before doing experiments')
        return redirect('/')

    if exp_id is None:
        flash('You must start a session before doing experiments.')
        return redirect('/')

    experiment = app.get_next(session)
    if experiment is None:
        flash('Congratulations, you have finished the battery!')
        return redirect('/finish')

    bot.log("<current:%s><next:%s>, <%s, %s>" %(last, next, subid, username))
    if do_redirect is True:
        return redirect(template)

    if context is not None and isinstance(context,dict):
        return render_template(template, **context)
    return render_template(template)


def clear_session():
    del session['subid']
    del session['username']
    del session['experiments']
    del session['exp_id']
