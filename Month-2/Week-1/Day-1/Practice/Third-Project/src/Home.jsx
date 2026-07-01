function Home(props){
    return(
        <div>
            This is the Home page
            <br />
            name : {props.name}
            <br />
            isPassed : {props.isPassed+""}
        </div>
    )
}
export default Home;