import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import Tooltip from '@material-ui/core/Tooltip';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Typography from '@material-ui/core/Typography';

const styles = theme => ({
    root: {
        margin : "auto",
        marginTop : theme.spacing.unit * 2,
        paddingTop: theme.spacing.unit * 2,
        paddingBottom: theme.spacing.unit * 2,
        paddingLeft: theme.spacing.unit * 2,
        paddingRight: theme.spacing.unit * 2,
        width : "80%",
        textAlign: "left",
    },
    heading: {
        fontSize: theme.typography.pxToRem(15),
        fontWeight: theme.typography.fontWeightRegular,
        textAlign: "left",
    },
});

class Review extends React.Component {

    constructor(props){
        super(props);

    }
    render() {
        const {classes} = this.props;
        return (
            <React.Fragment>
                    <List dense >
                        {this.props.responseState !== [] && this.props.responseState.map(value => (
                            <ExpansionPanel>
                                <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
                                    <Typography className={classes.heading}>{value.transaction.text}</Typography>
                                </ExpansionPanelSummary>
                                <ExpansionPanelDetails >
                                        {value.account_state.map(account => {
                                            return (
                                            <Typography variant="h8" gutterBottom className={classes.heading}>
                                                {"[ " + account.name + " " + account.ether  + " " +account.token + "] " }
                                            </Typography>
                                        )})}
                                </ExpansionPanelDetails>
                            </ExpansionPanel>

                        ))}
                    </List>
            </React.Fragment>
        );
    }
}
export default withStyles(styles)(Review);