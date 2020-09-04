%%%-------------------------------------------------------------------
%% @doc cicd public API
%% @end
%%%-------------------------------------------------------------------

-module(cicd_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    cicd_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
