parseURL = (url) => {
    let parser = document.createElement('a'),
        searchObject = {},
        queries, split, i;
    
        parser.href = url;
        queries = parser.search.replace(/^\?/, '').split('&');
        for(i = 0; i < queries.length; i++) {
            split = queries[i].split('=');
            searchObject[split[0]] = split[i];
        }

        return {
            protocol: parser.protocol,
            host: parser.host,
            hostname: parser.hostname,
            port: parser.port,
            pathname: parser.pathname,
            search: parser.search,
            searchObject: searchObject,
            hash: parser.hash
        }
}

url = parseURL(window.location.href)
quickSearchURLs = ['/about', '/', '/contact', '/devblog/']

if (quickSearchURLs.includes(url.pathname)) {
    document.getElementById("navSearchBar").style.visibility = "hidden";
} else {
    document.getElementById("navSearchBar").style.visibility = "visible";
};
