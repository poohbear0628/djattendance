import React, { PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SelectedEvent from './SelectedEvent'
import RollForm from './RollForm'

const ActionBar = ({submitRollShow, submitLeaveSlipShow, submitGroupLeaveSlipShow, otherReasonsShow, selectedEvents,
                    toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip, toggleOtherReasons,
                    removeSelectedEvent, removeAllSelectedEvents}) => {
  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }

  var showSection = {};
  if (submitRollShow) {
    showSection = {display: "none"};
  }

  return (
    <div style={{marginBottom: "10px"}}>
      <div>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitRoll}>Roll</Button>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitLeaveSlip}>Leave Slip</Button>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitGroupLeaveSlip}>Group Leave Slip</Button>
      </div>
      <div>
        <Collapse in={submitRollShow}>
          <div className="form-body">
            <div className="form-section bottom-border">
              <div className="toggle-title">
                Sessions Selected
                <Button bsSize="small" className={disabledClass} onClick={removeAllSelectedEvents}>Remove All</Button>
              </div>
              <div>
                {selectedEvents.map(function(ev) {
                  return <SelectedEvent
                            {...ev}
                            onClick={() => removeSelectedEvent(ev)}
                            selectedEvents={selectedEvents}
                          />
                })}
              </div>
            </div>
            <div className="form-section">
              <div className="toggle-title">Enter Roll</div>
              <RollForm />
              <div onClick={toggleSubmitLeaveSlip} className="checkbox-container leaveslip-checkbox">
                <input type="checkbox" checked={submitLeaveSlipShow}/> Leave Slip
              </div>
            </div>
          </div>
        </Collapse>
      </div>
      <div>
        <Collapse in={submitLeaveSlipShow}>
          <div className="form-body">
            <div className="form-section bottom-border" style={showSection}>
                <div className="toggle-title">
                  Sessions Selected
                  <Button bsSize="small" className={disabledClass} onClick={removeAllSelectedEvents}>Remove All</Button>
                </div>
                <div>
                  {selectedEvents.map(function(ev) {
                    return <SelectedEvent
                              {...ev}
                              onClick={() => removeSelectedEvent(ev)}
                              selectedEvents={selectedEvents}
                            />
                  })}
                </div>
              </div>
              <div className="form-section">
                <div className="toggle-title">Reason</div>
                <div data-toggle="buttons">
                  <div className="reason-container">
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Sickness </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Service </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Fellowship </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Night Out </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Meal Out </label>
                    <span onClick={toggleOtherReasons} className="checkbox-container">
                      <input type="checkbox" checked={otherReasonsShow}/> Other <span className="caret"></span>
                    </span>
                    <Collapse in={otherReasonsShow}>
                      <div data-toggle="buttons">
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Interview </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Gospel </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Conference </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Wedding </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Funeral </label>
                      </div>
                    </Collapse>
                  </div>
                  <div className="border-top">
                    <label className="notification-only"><input type="radio" name="options" autoComplete="off"/> Notification Only </label>
                  </div>
                </div>
                <div>
                  <div className="toggle-title">Comments</div>
                  <textarea className="comments-textarea"></textarea>
                </div>
                <div className="input-group">
                  <div className="input-group-btn">
                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">TA informed <span className="caret"></span></button>
                    <ul className="dropdown-menu">
                      <li><a href="#">TA informed</a></li>
                      <li><a href="#">Did not inform training office</a></li>
                      <li role="separator" className="divider"></li>
                      <OverlayTrigger trigger="hover" placement="bottom" overlay={<Popover id="att-num-pop" style={{width: 200}}>For sisters during non-Front Office hours only</Popover>}>
                        <li><a href="#">Texted attendance number</a></li>
                      </OverlayTrigger>
                    </ul>
                  </div>
                  <input type="text" className="form-control" aria-label="..."/>
                </div>
            </div>
            </div>
        </Collapse>
      </div>
      <div>
        <Collapse in={submitGroupLeaveSlipShow}>
          <div className="form-body">
            <div className="form-section bottom-border" style={showSection}>
                <div className="toggle-title">
                  Sessions Selected
                  <Button bsSize="small" className={disabledClass} onClick={removeAllSelectedEvents}>Remove All</Button>
                </div>
                <div>
                  {selectedEvents.map(function(ev) {
                    return <SelectedEvent
                              {...ev}
                              onClick={() => removeSelectedEvent(ev)}
                              selectedEvents={selectedEvents}
                            />
                  })}
                </div>
              </div>
              <div className="form-section">
                <div>
                  <div className="toggle-title">Trainees</div>
                  <textarea className="comments-textarea"></textarea>
                </div>
                <div className="toggle-title">Reason</div>
                <div data-toggle="buttons">
                  <div className="reason-container">
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Fellowship </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Service </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Conference </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Gospel </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Night Out </label>
                    <span onClick={toggleOtherReasons} className="checkbox-container">
                      <input type="checkbox" checked={otherReasonsShow}/> Other <span className="caret"></span>
                    </span>
                    <Collapse in={otherReasonsShow}>
                      <div data-toggle="buttons">
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Sickness </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Meal Out </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Interview </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Wedding </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Funeral </label>
                      </div>
                    </Collapse>
                  </div>
                  <div className="border-top">
                    <label className="notification-only"><input type="radio" name="options" autoComplete="off"/> Notification Only </label>
                  </div>
                </div>
                <div>
                  <div className="toggle-title">Comments</div>
                  <textarea className="comments-textarea"></textarea>
                </div>
                <div className="input-group">
                  <div className="input-group-btn">
                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">TA informed <span className="caret"></span></button>
                    <ul className="dropdown-menu">
                      <li><a href="#">TA informed</a></li>
                      <li><a href="#">Did not inform training office</a></li>
                      <li role="separator" className="divider"></li>
                      <OverlayTrigger trigger="hover" placement="bottom" overlay={<Popover id="att-num-pop" style={{width: 200}}>For sisters during non-Front Office hours only</Popover>}>
                        <li><a href="#">Texted attendance number</a></li>
                      </OverlayTrigger>
                    </ul>
                  </div>
                  <input type="text" className="form-control" aria-label="..."/>
                </div>
            </div>
            </div>
        </Collapse>
      </div>
    </div>
  )
}

ActionBar.propTypes = {
  submitRollShow: PropTypes.bool.isRequired, 
  submitLeaveSlipShow: PropTypes.bool.isRequired, 
  submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  toggleSubmitRoll: PropTypes.func.isRequired, 
  toggleSubmitLeaveSlip: PropTypes.func.isRequired, 
  toggleSubmitGroupLeaveSlip: PropTypes.func.isRequired
}

export default ActionBar
