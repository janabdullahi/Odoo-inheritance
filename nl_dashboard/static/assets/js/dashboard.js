function handle_params(url, param, value){
    if (url.has(param)) {
        url.set(param, value)
    } else {
        url.append(param, value)
    }
}

url = new URLSearchParams(window.location.search)
function handle_query(param, value, second_param='', second_value='') {
    handle_params(url, param, value)

    if (second_param){
        handle_params(url, second_param, second_value)
    }

    if (param.includes('_entries_limit') || param === 'filterby'){
        params = url.keys()
        for (const key of params) {
            if (key.includes('_page')){
                url.set(key, 1)
            }
        };
    }

    if (url.get('filterby') !== 'custom_date'){
        url.delete('from_date')
        url.delete('to_date')
    }

    window.location.replace(window.location.origin + window.location.pathname + '?' + url.toString())
}


document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};

function navigateDashboardKeepingCompanyAndFilterbyParameters(path){
    filterbyParam = ''
    companyParam = ''
    for (let entry of url.entries()) {
        if (entry[0] === 'company_id'){
            companyParam = `${entry[0]}=${entry[1]}`
        }
        if (entry[0] === 'filterby'){
            filterbyParam = `${entry[0]}=${entry[1]}`
        }
        if (entry[0] === 'from_date'){
            from_date = `${entry[0]}=${entry[1]}`
        }
        if (entry[0] === 'to_date'){
            to_date = `${entry[0]}=${entry[1]}`
        }
    }
    if (filterbyParam && companyParam){
        search = `?${companyParam}&${filterbyParam}`
    } else if (filterbyParam && !companyParam){
        search = `?${filterbyParam}`
    } else if (companyParam && !filterbyParam){
        search = `?${companyParam}`
    } else {
        search = ''
    }
    if (url.get('filterby') === 'custom_date'){
        search = `${search}&${from_date}&${to_date}`
    }
    window.location.replace(`${window.location.origin}/${path}${search}`)
}

function makeCustomDateSearch(){
    from = document.querySelector('.from-date')
    to = document.querySelector('.to-date')
    to.min = from.value
    from.max = to.value

    if (from.value && to.value) {
        handle_params(url, 'filterby', 'custom_date')
        handle_params(url, 'from_date', from.value)
        handle_params(url, 'to_date', to.value)
        window.location.replace(window.location.origin + window.location.pathname + '?' + url.toString())
    }
}